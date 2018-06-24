import io
import ConfigParser

sample_config = """
[mysqld]
user1=%(user)rabc
user=mysql
pid-file = /var/run/mysqld/mysqld.pid
skip-external-locking
old_passwords = 1
skip-bdb
skip-innodb
"""
# config = ConfigParser.RawConfigParser(allow_no_value=True)
config = ConfigParser.ConfigParser(allow_no_value=True)
config.readfp(io.BytesIO(sample_config))

# # Settings with values are treated as before:
config.get("mysqld", "user")
#
# # Settings without values provide None:
# config.get("mysqld", "skip-bdb")
#
# # Settings which aren't specified still raise an error:
# config.get("mysqld", "does-not-exist")
