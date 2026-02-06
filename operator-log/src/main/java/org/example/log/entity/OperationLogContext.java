package org.example.log.entity;

import lombok.Builder;
import lombok.Data;
import org.example.log.annotation.OperationLog;

/**
 * @author aengus
 */
@Data
@Builder
public class OperationLogContext {

    private OperationLog operationLog;

    private Object beforeObj;
    private Object afterObj;

    private String username;

    private Throwable bizException;

    private String traceId;

    private boolean batch;

    private String parsedCondition;

    private Integer affectRows;

}

