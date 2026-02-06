package org.example.entity;

import lombok.Data;

import java.util.List;

@Data
public class UserLoginReq {

    private Integer id;
    private String username;
    private String password;

}
