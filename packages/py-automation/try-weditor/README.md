# try-weditor

Describe your project here.

## Usage:

### 使用 weditor 调试 android app

- run tool

```ruby

weditor

```

- run :

```ruby

# venv activate: 
source .venv/bin/activate.fish

# run:
task auto:we:r

```

## Fix:

### 报错:

- 查看设备 shell:

```ruby
adb -s 10.211.1.129:41941 shell


# under android shell:
alioth:/ $ ps -u shell
USER           PID  PPID     VSZ    RSS WCHAN            ADDR S NAME                       
shell          980 20571 2193256   2704 __arm64_s+          0 S sh
shell          984   980 5766832 101948 futex_wai+          0 S app_process
shell        11246 20571 2168680   2768 __arm64_s+          0 S sh
shell        11255 11246 2179616   3480 0                   0 R ps
shell        20571     1 2362820   8580 0                   0 S adbd

# 说明有 2 个 sh 在运行(因为开了另外一个服务, 先关闭, 才能运行本代码)

# 关闭后, 正常状态:
alioth:/ $ ps -u shell                                                                                                                                                                                               
USER           PID  PPID     VSZ    RSS WCHAN            ADDR S NAME                       
shell        11246 20571 2168680   3216 __arm64_s+          0 S sh
shell        11408 11246 2228768   3436 0                   0 R ps
shell        20571     1 2345384   8568 0                   0 S adbd

  
```

- 正确获得设备信息:

```json5


{
    'currentPackageName': 'com.miui.home',
    'displayHeight': 2400,
    'displayRotation': 0,
    'displaySizeDpX': 393,
    'displaySizeDpY': 873,
    'displayWidth': 1080,
    'productName': 'alioth',
    'screenOn': True,
    'sdkInt': 33,
    'naturalOrientation': True
}


```

## Reference

- https://github.com/alibaba/web-editor


