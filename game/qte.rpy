screen qte_keyboard:
    #key input qte

    timer interval repeat True action If(time_start > 0.0, true=SetVariable('time_start', time_start - interval), false=[Return(0), Hide('qte_keyboard')])
    # timer, using variables from label qte_setup
    # false is the condition if the timer runs out - and this will be reached if the user doesn't get hit the key on time

    key trigger_key action ( Play("sound", "audio/hit.mp3"), Return(1) )
    # the "key detector" (plays sound and ends qte_event by returning 1)

    vbox:
        xalign x_align
        yalign y_align
        spacing 25
        # vbox arrangement

        text trigger_key:
            xalign 0.5
            color "#fff"
            size 36
            #outlines [ (2,"#000000",0,0) ]
            # text showing the key to press

        bar:
            value time_start
            range time_max
            xalign 0.5
            xmaximum 300
            if time_start < (time_max * 0.25):
                left_bar "#f00"
                # this is the part that changes the colour to red if the time reaches less than 25%


screen qte_button1:
    #button press qte

    button:
        action Return(0) #miss
        align 0.5, 0.5

        #to add a click sensor *outside* of button (if player presses outside button area) and return false


    timer interval repeat True action If(time_start > 0.0, true=SetVariable('time_start', time_start - interval), false=[Return(0), Hide('qte_button')])
    #see above

    vbox:
        xalign x_align yalign y_align spacing 25

        button:
            action Return(1)
            xalign 0.5
            xysize 75, 75
            activate_sound "audio/выстрел.mp3"
            #same function as the key input


        bar:
            value time_start
            range time_max
            xalign 0.2
            xmaximum 300
            if time_start < (time_max * 0.25):
                left_bar "#f00"

screen qte_button2:
    #button press qte

    button:
        action Return(0) #miss
        align 0.5, 0.5
        #to add a click sensor *outside* of button (if player presses outside button area) and return false


    timer interval repeat True action If(time_start > 0.0, true=SetVariable('time_start', time_start - interval), false=[Return(0), Hide('qte_button')])
    #see above

    vbox:
        xalign x_align yalign y_align spacing 25

        button:
            action Return(1)
            xalign 0.5
            xysize 150, 225
            activate_sound "audio/выстрел.mp3"
            #same function as the key input


        bar:
            value time_start
            range time_max
            xalign 0.2
            xmaximum 300
            if time_start < (time_max * 0.25):
                left_bar "#f00"
