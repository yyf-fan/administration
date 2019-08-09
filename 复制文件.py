src_filename = input('请输入源文件路径名:')
dst_filename = input('请输入目标文件路径名:')

try:  # 防止打开源文件失败
    src = open(src_filename,'rb')  # 打开源文件用来读数据
    try:  # 防止打开写入文件失败
        try:
            dst = open(dst_filename,'wb')  # 打开目标文件用来写数据
            try:
                while True:
                    # 考虑特大文件
                    b = src.read(4096)
                    if not b:  # 已经读取完毕
                        break
                        dst.write(b)
            finally:
                dst.close()
                print('复制成功')
        except OSError:
            print('打开写入文件失败')
    finally:
        src.close()
except OSError:
    print('复制失败')
