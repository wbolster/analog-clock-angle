
def calculate_angle(time):
    """
    Calculate the angle between the two hands of an analog clock.
    The time should be specified as a string in HH:MM format, and the
    answer is in degrees.
    """

    hours, minutes = [int(chunk) for chunk in time.split(':', 1)]
    assert 0 <= hours < 24
    assert 0 <= minutes < 60

    # A day has 24 hours, but a clock rotates in only 12
    hours = hours % 12

    # Calculate angles for both hands, both relative to 0:00 position,
    # by calculating the elapsed proportion of a full circle (12 hours).
    minutes_elapsed_since_noon = hours * 60 + minutes
    minutes_angle = minutes * (360. / 60)
    hours_angle = minutes_elapsed_since_noon * 360. / (60 * 12)

    # Combine and make sure we always return the "inner" (smaller) angle
    angle = (hours_angle - minutes_angle) % 360
    if angle > 180:
        angle = 360 - angle

    assert 0 <= angle <= 180
    return angle


if __name__ == '__main__':
    print "Angle is %.1f deg" % calculate_angle(raw_input("Time (HH:MM)? "))
