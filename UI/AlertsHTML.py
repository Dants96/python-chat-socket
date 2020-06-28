
__alertFail_class = "color: red; font-size:14px;font-weight: bold;"
__alertsucces_class = "color: green; font-size:14px;font-weight: bold;"
__alertinfo_class = "color: blue"
__alertFail2_class = "color: red"

def alertFail(msg):
    return "<div style=\"{0}\">{1}!</div>".format(__alertFail_class, msg)

def alertSucces(msg):
    return "<div style=\"{0}\">{1}</div>".format(__alertsucces_class, msg)

def alertInfo(msg):
    return "<div style=\"{0}\">{1}</div>".format(__alertinfo_class, msg)

def alertFail2(msg):
    return "<div style=\"{0}\">{1}!</div>".format(__alertFail2_class, msg)