package org.example.log.utils;

import org.aspectj.lang.JoinPoint;
import org.aspectj.lang.reflect.MethodSignature;
import org.springframework.core.DefaultParameterNameDiscoverer;
import org.springframework.core.ParameterNameDiscoverer;
import org.springframework.expression.EvaluationContext;
import org.springframework.expression.Expression;
import org.springframework.expression.ExpressionParser;
import org.springframework.expression.spel.standard.SpelExpressionParser;
import org.springframework.expression.spel.support.StandardEvaluationContext;

public class SpELUtils {

    // 表达式解析器
    private static final ExpressionParser parser = new SpelExpressionParser();

    // 参数名解析器，用于拿到方法参数名
    private static final ParameterNameDiscoverer nameDiscoverer =
            new DefaultParameterNameDiscoverer();

    public static String parse(String spel, JoinPoint jp) {

        // 如果不是 SpEL，直接返回（例如直接写 "固定ID"）
        if (spel == null || spel.isEmpty() || !spel.startsWith("#")) {
            return spel;
        }

        MethodSignature signature = (MethodSignature) jp.getSignature();
        String[] paramNames = nameDiscoverer.getParameterNames(signature.getMethod());

        EvaluationContext ctx = new StandardEvaluationContext();
        Object[] args = jp.getArgs();

        // 绑定方法参数到 SpEL 上下文
        if (paramNames != null) {
            for (int i = 0; i < paramNames.length; i++) {
                ctx.setVariable(paramNames[i], args[i]);
            }
        }

        // 执行 SpEL 表达式
        Expression expression = parser.parseExpression(spel);
        Object value = expression.getValue(ctx);

        return value == null ? null : value.toString();
    }

    public static Object parseRaw(String spel, JoinPoint jp) {

        MethodSignature signature = (MethodSignature) jp.getSignature();
        String[] paramNames = nameDiscoverer.getParameterNames(signature.getMethod());

        EvaluationContext ctx = new StandardEvaluationContext();
        Object[] args = jp.getArgs();

        if (paramNames != null) {
            for (int i = 0; i < paramNames.length; i++) {
                ctx.setVariable(paramNames[i], args[i]);
            }
        }

        Expression expression = parser.parseExpression(spel);
        return expression.getValue(ctx);
    }

    public static Object parseRaw(String spel, JoinPoint jp, Object retVal) {
        if (spel == null || spel.isEmpty() || !spel.startsWith("#")) {
            return spel;
        }

        MethodSignature signature = (MethodSignature) jp.getSignature();
        String[] paramNames = nameDiscoverer.getParameterNames(signature.getMethod());
        Object[] args = jp.getArgs();

        EvaluationContext ctx = new StandardEvaluationContext();

        // 方法参数
        if (paramNames != null) {
            for (int i = 0; i < paramNames.length; i++) {
                ctx.setVariable(paramNames[i], args[i]);
            }
        }

        // 返回值（INSERT 必用）
        ctx.setVariable("_ret", retVal);
        Expression expression = parser.parseExpression(spel);
        return expression.getValue(ctx);
    }


}
