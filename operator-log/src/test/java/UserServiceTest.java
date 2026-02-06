import jakarta.annotation.Resource;
import lombok.extern.slf4j.Slf4j;
import org.example.LogApplication;
import org.example.log.mapper.UserMapper;
import org.example.log.service.UserService;
import org.junit.jupiter.api.Test;
import org.springframework.boot.test.context.SpringBootTest;

import java.util.Arrays;
import java.util.List;

@Slf4j
@SpringBootTest(classes = LogApplication.class)
class UserServiceTest {

    @Resource
    private UserService userService;

    @Resource
    private UserMapper userMapper;

    /**
     * 测试：新增用户（INSERT）
     */
    @Test
    void testCreateUser() {
        Long userId = userService.createUser("张三", 20);
        log.info("创建用户成功，id={}", userId);
    }

    /**
     * 测试：更新用户（UPDATE + diff）
     */
    @Test
    void testUpdateUser() {
        // 先准备一条数据
        Long userId = userService.createUser("李四", 25);

        // 更新
        userService.updateUser(userId, "李四-修改", 26, 1);

        log.info("更新用户完成，id={}", userId);
    }

    /**
     * 测试：删除用户（DELETE）
     */
    @Test
    void testDeleteUser() {
        Long userId = userService.createUser("王五", 30);
        userService.deleteUser(userId);
        log.info("删除用户完成，id={}", userId);
    }

    /**
     * 测试：批量禁用用户（BATCH）
     */
    @Test
    void testBatchDisableUsers() {
        Long id1 = userService.createUser("用户A", 18);
        Long id2 = userService.createUser("用户B", 19);

        List<Long> ids = Arrays.asList(id1, id2);
        int count = userService.batchDisableUsers(ids);

        log.info("批量禁用完成，影响条数={}", count);
    }

    /**
     * 测试：批量删除无效用户（BATCH）
     */
    @Test
    void testBatchDeleteInactiveUsers() {
        List<Long> ids = Arrays.asList(8L, 9L);
        int count = userService.batchDeleteInactiveUsers(ids);
        log.info("批量删除无效用户完成，影响条数={}", count);
    }
}
