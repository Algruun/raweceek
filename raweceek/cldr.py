from icalevents.icalevents import events


# rework method
async def get_events() -> list[str]:
    this_week = []
    # change link to config variable
    es = events('http://www.formula1.com/calendar/Formula_1_Official_Calendar.ics', fix_apple=True)
    # shit bellow
    for i in es:
        if i.summary.split(' ')[-1] in ['Race', 'Qualifying']:
            date = str(i.start).replace('-', '\-').replace('+', '\+')
            text = i.summary.replace('-', '\-')
            this_week.append(f'{date}\n{text}')
    return this_week
