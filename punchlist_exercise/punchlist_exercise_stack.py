from aws_cdk import (
    # Duration,
    Stack,
    CfnOutput,
    aws_ec2 as ec2,
    aws_ecs as ecs,
    aws_ecs_patterns as ecs_patterns
)
from constructs import Construct

class PunchlistExerciseStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # The code that defines your stack goes here

        vpc = ec2.Vpc(self, "VpcPunchList", max_azs=2)     # default is all AZs in region

        cluster = ecs.Cluster(self, "ClusterPunchList", vpc=vpc)

        fargate_service = ecs_patterns.ApplicationLoadBalancedFargateService(
            self, "FargateService",
            cluster=cluster,
            cpu=1024,
            memory_limit_mib=2048,
            task_image_options={
                'image': ecs.ContainerImage.from_asset('./hello-spring'),
                'container_port': 8080
            }
        )

        fargate_service.service.connections.security_groups[0].add_ingress_rule(
            peer = ec2.Peer.ipv4(vpc.vpc_cidr_block),
            connection = ec2.Port.tcp(80),
            description="Allow http inbound from VPC"
        )

        fargate_service.target_group.configure_health_check(
            healthy_http_codes="200",
            port="8080",
            path="/"
        )

        CfnOutput(
            self, "LoadBalancerDNS",
            value=fargate_service.load_balancer.load_balancer_dns_name
        )