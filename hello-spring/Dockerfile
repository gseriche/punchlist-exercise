FROM maven:3-openjdk-8-slim as builder

COPY src /usr/src/app/src
COPY pom.xml /usr/src/app

RUN mvn -f /usr/src/app/pom.xml clean package

FROM openjdk:8-jre-alpine
EXPOSE 8080

COPY --from=builder /usr/src/app/target/spring-boot-complete-0.0.1-SNAPSHOT.jar /usr/app/spring-boot-complete-0.0.1-SNAPSHOT.jar

ENTRYPOINT ["java", "-jar", "/usr/app/spring-boot-complete-0.0.1-SNAPSHOT.jar"]

