import io.github.yedaxia.apidocs.Docs;
import io.github.yedaxia.apidocs.DocsConfig;

public class ApiDocTest {


    public static void main(String[] args) {
        DocsConfig config = new DocsConfig();
        config.setProjectPath("D:\\work\\projects\\figer\\google-auth\\src\\main\\java\\org"); // 如：F:\\project\\src
        config.setProjectName("测试项目");
        config.setApiVersion("V1.0");
        config.setDocsPath("D:\\doc"); // 如：F:\\api_docs
        config.setAutoGenerate(true); // 开启自动生成
        Docs.buildHtmlDocs(config); // 执行生成

    }

}
