package org.example.log.utils;

import org.slf4j.MDC;

import java.util.UUID;

/**
 * @author aengus
 */
public class TraceIdUtils {

    public static final String TRACE_ID = "traceId";

    public static String getOrCreate() {
        String traceId = MDC.get(TRACE_ID);
        if (traceId == null) {
            traceId = UUID.randomUUID().toString().replace("-", "");
            MDC.put(TRACE_ID, traceId);
        }
        return traceId;
    }
}
