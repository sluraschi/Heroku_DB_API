SEISMIC_DATABASE_HOST = "ec2-174-129-254-216.compute-1.amazonaws.com"
SEISMIC_DATABASE = "dffja4igmjagb2"

TEMPERATURE_DATABASE_HOST = "ec2-18-233-32-61.compute-1.amazonaws.com"
TEMPERATURE_DATABASE = "d6b6g9o80ao27h"

PACKAGE_TABLE_NAME = "package"
SEGMENT_TABLE_NAME = "segment"

PACKAGE_INSERT_QUERY = f"INSERT INTO {PACKAGE_TABLE_NAME} (date, id, length) VALUES (%s, %s, %s)"
SEGMENT_INSERT_QUERY = f"INSERT INTO {SEGMENT_TABLE_NAME} (package_id, id, " \
                       f"date, microsec, rate, flag1, flag2, flag3, flag4) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)"