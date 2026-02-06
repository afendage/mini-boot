package org.example;

import org.mybatis.spring.annotation.MapperScan;
import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;

/**
 * @author aengus
 */
@SpringBootApplication
@MapperScan("org.example.log.mapper")
public class LogApplication {
    public static void main(String[] args) {
        SpringApplication.run(LogApplication.class, args);
    }
}