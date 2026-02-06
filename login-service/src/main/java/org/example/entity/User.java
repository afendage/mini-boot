package org.example.entity;

import lombok.Data;

@Data
public class User {
    private Long id;
    private String username;
    private String password;
    private String nickname;
    private String role; // 角色（多个角色用逗号分隔）
}
