def convert_bytes(size) -> str:
        # CJM - 2022/06/10:
        # Convert bytes to KB, or MB or GB
        for x in ["bytes", "KB", "MB", "GB", "TB"]:
            if size < 1024.0:
                return "%3.1f %s" % (size, x)
            size /= 1024.0

  