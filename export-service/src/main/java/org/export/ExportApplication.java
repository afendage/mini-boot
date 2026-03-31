package org.export;

import org.mybatis.spring.annotation.MapperScan;
import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.scheduling.annotation.EnableAsync;

/**
 * @author Aengus
 */
@SpringBootApplication
@EnableAsync
@MapperScan("org.export.mapper")
public class ExportApplication {
    public static void main(String[] args) {
        SpringApplication.run(ExportApplication.class, args);
    }
}