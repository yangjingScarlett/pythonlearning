import sys

print sys.getdefaultencoding()
reload(sys)

sys.setdefaultencoding('utf-8')
print sys.getdefaultencoding()

