from controller import CodeAudit

if __name__ == "__main__":
    f = CodeAudit.FileList("C:\phpStudy\PHPTutorial\WWW\phpScaner", "func.txt")
    f.audit_init()