
import org.junit.Test;
import java.util.regex.Pattern;

public class PrivacyMasker {

    // 邮箱正则验证
    private static final String EMAIL_REGEX = "^[A-Za-z0-9+_.-]+@[A-Za-z0-9.-]+\\.[A-Za-z]{2,}$";
    private static final Pattern EMAIL_PATTERN = Pattern.compile(EMAIL_REGEX);

    @Test
    public void tt(){
        System.out.println(this.maskPhone("1254"));
        System.out.println(this.maskEmail("wr@qq.com"));
    }

    /**
     * 手机号脱敏处理
     * @param phone 原始手机号
     * @return 脱敏后的手机号，格式如：188****0785
     */
    public static String maskPhone(String phone) {
        if (phone == null || phone.trim().isEmpty()) {
            throw new IllegalArgumentException("手机号不能为空");
        }
        String cleanPhone = phone.trim();
        if(cleanPhone.length()<6){
            return cleanPhone.charAt(0) + "****";
        }
        // 保留前3位和后4位，中间4位用*代替
        return cleanPhone.substring(0, 3) + "****" + cleanPhone.substring(7);
    }

    /**
     * 邮箱脱敏处理
     * @param email 原始邮箱
     * @return 脱敏后的邮箱，格式如：380****399@qq.com
     */
    public static String maskEmail(String email) {
        if (email == null || email.trim().isEmpty()) {
            throw new IllegalArgumentException("邮箱不能为空");
        }

        String cleanEmail = email.trim();
        if (!EMAIL_PATTERN.matcher(cleanEmail).matches()) {
            throw new IllegalArgumentException("请输入有效的邮箱地址");
        }

        int atIndex = cleanEmail.indexOf('@');
        if (atIndex == -1) {
            throw new IllegalArgumentException("邮箱格式不正确");
        }

        String username = cleanEmail.substring(0, atIndex);
        String domain = cleanEmail.substring(atIndex);

        // 根据用户名长度决定隐藏位数
        if (username.length() <= 3) {
            return "***" + domain;
        } else if (username.length() <= 6) {
            String prefix = username.substring(0, 2);
            return prefix + "***" + domain;
        } else {
            // 保留前3位和后3位，中间用*代替
            String prefix = username.substring(0, 3);
            String suffix = username.length() > 6 ? username.substring(username.length() - 3) : "";
            return prefix + "****" + suffix + domain;
        }
    }

}
