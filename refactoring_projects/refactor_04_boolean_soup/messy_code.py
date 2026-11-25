# Legacy OrbitalGo launch readiness check.
# Just to be 1000% sure a True is REALLY True, we check it with == True!


def can_launch_rocket(fuel_pct, weather_clear, crew_ready, override_code):
    fuel_ok = False
    if fuel_pct >= 80:
        fuel_ok = True
    else:
        fuel_ok = False

    override_valid = False
    if override_code == "ALPHA-9":
        override_valid = True

    ready_flag = False
    if fuel_ok == True:
        if crew_ready == True:
            if weather_clear == True:
                ready_flag = True
            elif weather_clear == False:
                if override_valid == True:
                    ready_flag = True
                else:
                    ready_flag = False
        else:
            ready_flag = False
    else:
        ready_flag = False

    if ready_flag == True:
        return True
    else:
        return False
