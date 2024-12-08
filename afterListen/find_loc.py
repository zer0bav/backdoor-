import gps

def loc_ff():
    session = gps.gps(mode=gps.WATCH_ENABLE | gps.WATCH_NEWSTYLE)
    report = session.next()
    if report['class'] == 'TPV':
        latitude = getattr(report, 'lat', "Unknown")
        longitude = getattr(report, 'lon', "Unknown")
        time = getattr(report, 'time', "Unknown")
        return f"Time: {time}, Latitude: {latitude}, Longitude: {longitude}"
