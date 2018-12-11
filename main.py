from controller import CodeAudit

if __name__ == "__main__":
    f = CodeAudit.FileList("C:\phpStudy\PHPTutorial\WWW\phpScaner", "func.json")
    f.audit_init()