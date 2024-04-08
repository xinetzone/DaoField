# FAQs

## 详解 shell 中 `source`、`sh`、`bash`、`./` 执行脚本的区别

### `source` 命令用法

```bash
source FileName
```

作用：在当前 `bash` 环境下读取并执行 `FileName` 中的命令。该 `FileName` 文件可以无"执行权限"

注：该命令通常用命令“`.`”来替代。

如：`source .bash_profile` 和 `. .bash_profile` 两者等效。

`source`(或 `.`) 命令通常用于重新执行刚修改的初始化文档。

- `source` 命令 (从 C Shell 而来)是 bash shell 的内置命令。
- `.` 命令，就是个点符号，(从 Bourne Shell 而来)。

### `sh` 和 `bash` 命令用法

```bash
sh FileName
```

或者

```bash
bash FileName
```

作用：在当前 `bash` 环境下读取并执行 `FileName` 中的命令。该 `FileName` 文件可以无"执行权限"

注：两者在执行文件时的不同，是分别用自己的 shell 来跑文件。

`sh` 使用“`-n`”选项进行 shell 脚本的语法检查，使用“`-x`”选项实现shell脚本逐条语句的跟踪，可以巧妙地利用shell的内置变量增强“`-x`”选项的输出信息等。

### `./` 的命令用法

```bash
./FileName
```

作用：打开一个子 shell 来读取并执行 `FileName` 中命令。

注：运行一个 shell 脚本时会启动另一个命令解释器。

每个 shell 脚本有效地运行在父 shell (parent shell)的一个子进程里。

这个父 shell 是指在一个控制终端或在一个 xterm 窗口中给你命令指示符的进程。

shell 脚本也可以启动他自已的子进程。

这些子 shell (即子进程)使脚本并行地，有效率地地同时运行脚本内的多个子任务。

### shell的嵌入命令

```bash
:        空，永远返回为true
.        从当前shell中执行操作
break    退出for、while、until或case语句
cd       改变到当前目录
continue 执行循环的下一步
echo     反馈信息到标准输出
eval     读取参数，执行结果命令
exec     执行命令，但不在当前shell
exit     退出当前shell
export   导出变量，使当前shell可利用它
pwd      显示当前目录
read     从标准输入读取一行文本
readonly 使变量只读
return   退出函数并带有返回值
set      控制各种参数到标准输出的显示
shift    命令行参数向左偏移一个
test     评估条件表达式
times    显示shell运行过程的用户和系统时间
trap     当捕获信号时运行指定命令
ulimit   显示或设置shell资源
umask    显示或设置缺省文件创建模式
unset    从shell内存中删除变量或函数
wait     等待直到子进程运行完毕
```

```{topic} 小结
shell 脚本各种执行方式（`source ./*.sh`, `. ./*.sh`, `./*.sh`）的区别

- 结论一： `./*.sh` 的执行方式等价于 `sh ./*.sh` 或者 `bash ./*.sh`，此三种执行脚本的方式都是重新启动一个子 shell，在子 shell 中执行此脚本，脚本中设置的变量在脚本执行完毕后不会保存。但是若 `script.sh` 脚本不是以 `#!/bin/bash` 开头，那么也不会在子进程中执行。
- 结论二： `source ./*.sh` 和 `. ./*.sh` 的执行方式是等价的，即两种执行方式都是在当前 shell 进程中执行此脚本，而不是重新启动一个 shell 在子 shell 进程中执行此脚本，并且脚本中设置的变量在脚本执行完毕后会保存下来。
```

验证依据：没有被 `export` 导出的变量（即非环境变量）是不能被子 shell 继承的
