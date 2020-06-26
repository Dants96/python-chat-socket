
_alertFail_class = "color: red; font-size:14px;font-weight: bold;"
_alertsucces_class = "color: green; font-size:14px;font-weight: bold;"
_alertinfo_class = "color: blue"

def alertFail(msg):
    return "<div style=\"{0}\">{1}!</div>".format(_alertFail_class, msg)

def alertSucces(msg):
    return "<div style=\"{0}\">{1}</div>".format(_alertsucces_class, msg)

def alertInfo(msg):
    return "<div style=\"{0}\">{1}</div>".format(_alertinfo_class, msg)