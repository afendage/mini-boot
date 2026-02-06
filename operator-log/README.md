# Operation Log 操作日志组件

基于 Spring AOP + MyBatis Plus 的通用操作日志组件，用于统一记录系统中的新增、修改、删除以及批量操作行为，适合用于审计、问题排查和业务回溯场景。该组件强调日志准确性与可回溯性，避免因参数不完整或业务变更导致日志失真。

该组件支持 INSERT / UPDATE / DELETE / BATCH 四种操作类型，支持修改和删除操作自动回查数据库获取操作前数据（before_value），支持新增操作使用返回主键进行回查，确保 after_value 为数据库真实数据。日志写入采用异步方式，不影响主业务事务，并支持链路追踪 TraceId。

核心使用方式通过 @OperationLog 注解完成。

注解字段说明如下：

module 表示模块编码，用于区分业务模块
moduleName 表示模块名称，用于展示
type 表示操作类型，可选 INSERT、UPDATE、DELETE、BATCH
typeName 表示操作类型的中文描述
entity 表示对应的数据库实体类，用于回查 before 或 after 数据
id 表示主键的 SpEL 表达式，例如 #id、#user.id
fieldNames 用于指定需要记录差异的字段，格式为 字段名:展示名
condition 用于批量操作的条件描述
remark 为扩展备注字段

新增（INSERT）操作推荐使用回查模式，方法必须返回新增数据的主键 ID，日志会在方法执行完成后，使用返回的 ID 回查数据库作为 after_value，避免仅使用参数造成字段缺失。

示例：

@OperationLog(
    module = "USER",
    moduleName = "用户管理",
    type = OperateType.INSERT,
    typeName = "新增用户",
    entity = User.class
)

该模式下 before_value 不记录，after_value 为数据库真实数据，diff_value 不生成。

修改（UPDATE）操作通常需要记录修改前后的差异。推荐配置 entity 和 id，用于在方法执行前回查数据库获取 before_value。修改完成后再回查数据库获取 after_value。

如果希望只记录指定字段的变化，可以通过 fieldNames 指定需要对比的字段。

示例：

@OperationLog(
    module = "USER",
    moduleName = "用户管理",
    type = OperateType.UPDATE,
    typeName = "修改用户信息",
    entity = User.class,
    id = "#id",
    fieldNames = {
        "name:姓名",
        "age:年龄",
        "status:状态"
    }
)

此时 before_value 为修改前数据库数据，after_value 为修改后数据库数据，diff_value 仅包含指定字段的变化。

如果不配置 fieldNames，则默认启用全字段自动差异对比，系统会对比 before 和 after 的所有字段，仅记录发生变化的字段。

示例：

@OperationLog(
    module = "USER",
    moduleName = "用户管理",
    type = OperateType.UPDATE,
    typeName = "修改用户信息",
    entity = User.class,
    id = "#id"
)

删除（DELETE）操作需要记录删除前的数据状态，因此必须配置 entity 和 id。系统会在删除前回查数据库作为 before_value，after_value 不记录。

示例：

@OperationLog(
    module = "USER",
    moduleName = "用户管理",
    type = OperateType.DELETE,
    typeName = "删除用户",
    entity = User.class,
    id = "#id"
)

批量操作（BATCH）用于无法逐条记录明细的场景，只记录操作条件与影响行数，不记录 before 和 after 的具体数据。

如果批量条件来自方法参数，可以直接使用 SpEL 表达式引用参数。

示例：

@OperationLog(
    module = "USER",
    moduleName = "用户管理",
    type = OperateType.BATCH,
    typeName = "批量禁用用户",
    condition = "#ids"
)

如果条件为固定值，也可以直接写字符串。

示例：

@OperationLog(
    module = "USER",
    moduleName = "用户管理",
    type = OperateType.BATCH,
    typeName = "批量删除无效用户",
    condition = "status = 0"
)

SpEL 表达式支持方法参数名和对象属性访问。例如：

id = "#id"           对应方法参数 Long id
id = "#user.id"      对应方法参数 User user
condition = "#ids"   对应方法参数 List<Long> ids

设计约定如下：

INSERT 操作优先使用返回值回查数据库作为 after_value
UPDATE / DELETE 操作的 before_value 一定来自数据库
UPDATE 的 diff_value 只记录发生变化的字段
BATCH 操作仅记录 condition 和 affectRows
日志写入失败不会影响业务事务
after_value 不直接信任方法参数，避免脏数据或缺字段


