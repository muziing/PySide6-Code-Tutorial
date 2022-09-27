# QDir.Filters

<https://doc.qt.io/qt-6/qdir.html#Filter-enum>

| 常量           | 值                      | 描述                                                         |
| -------------- | ----------------------- | ------------------------------------------------------------ |
| Dirs           | 0x001                   | 列出与过滤器匹配的目录                                       |
| AllDirs        | 0x400                   | 列出所有目录，即不对目录名使用过滤器                         |
| Files          | 0x002                   | 列出文件                                                     |
| Drives         | 0x004                   | 列出磁盘驱动器（在Unix下忽略）                               |
| NoSymLinks     | 0x008                   | 不要列出符号链接（在不支持符号链接的操作系统上忽略）         |
| NoDotAndDotDot | NoDot \| NoDotDot       | 不要列出特殊条目"."和".."                                    |
| NoDot          | 0x2000                  | 不要列出特殊条目"."                                          |
| NoDotDot       | 0x4000                  | 不要列出特殊条目".."                                         |
| AllEntries     | Dirs \| Files \| Drives | 列出目录、文件、驱动器和符号链接（除非指定System,否则不会列出损坏的符号链接） |
| Readable       | 0x010                   | 列出应用程序对其具有读取权限的文件。需要与Dirs或Files结合使用 |
| Writable       | 0x020                   | 列出应用程序对其具有写入权限的文件。需要与Dirs或Files结合使用 |
| Executable     | 0x040                   | 列出应用程序对其具有执行权限的文件。需要与Dirs或Files结合使用 |
| Modified       | 0x080                   | 仅列出已修改的文件（在Unix上忽略）                           |
| Hidden         | 0x100                   | 列出隐藏文件（在Unix平台上那些以"."开头的文件）              |
| System         | 0x200                   | 列出系统文件（在Unix上包括FIFO、套接字和设备文件；在Windows上包括.lnk文件） |
| CaseSensitive  | 0x800                   | 过滤器区分大小写                                             |
