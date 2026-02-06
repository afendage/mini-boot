package org.example.controller;

import org.example.config.JwtUtils;
import org.example.entity.UserLoginReq;
import org.example.service.UserService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.security.access.prepost.PreAuthorize;
import org.springframework.security.authentication.AuthenticationManager;
import org.springframework.security.authentication.UsernamePasswordAuthenticationToken;
import org.springframework.security.core.Authentication;
import org.springframework.security.core.context.SecurityContextHolder;
import org.springframework.security.core.userdetails.UserDetails;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RestController;

@RestController
public class LoginController {

    @Autowired
    private AuthenticationManager authenticationManager;
    @Autowired
    private UserService userService;
    @Autowired
    private JwtUtils jwtUtils;

    // 登录接口
    @GetMapping("/login")
    public String login(@RequestBody UserLoginReq req) {
        // 1. 认证用户名密码
        Authentication authentication = authenticationManager.authenticate(
                new UsernamePasswordAuthenticationToken(req.getUsername(), req.getPassword())
        );
        // 2. 生成 JWT 令牌
        SecurityContextHolder.getContext().setAuthentication(authentication);
        UserDetails userDetails = (UserDetails) authentication.getPrincipal();
        String token = jwtUtils.generateToken(userDetails.getUsername());
        return token;
    }

    // 测试接口（需认证）
    @GetMapping("/hello")
//    @PreAuthorize("hasRole('USER')") // 仅允许 USER 角色访问
    public String hello() {
        return SecurityContextHolder.getContext().getAuthentication().getName();
    }
}
