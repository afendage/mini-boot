package org.example.service;

import org.example.service.impl.GoogleAuthServiceImpl;

public interface GoogleAuthService {
    
    GoogleAuthServiceImpl.GoogleAuthResult generateKey(String username, String issuer);

    public boolean verifyCode(String secretKey, int code);

}
