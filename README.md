# django-customtags-filters

# {{ }} -------> filter

# {% %} -------> tag
 # Step for Custom filter

 ```
 -->1:
    create project
    -->2:
        create app
            # views.py
            from django.shortcuts import render

            # Create your views here.
            def HomeView(request):
                return render(request, 'home.html', context={'data':'amaer deshe hobe sei cele kobe j kothai na boro hoye kaje boro hobe.', 't':20,})

    -->3:
        create templatetags dir inside app dir

        -->4: 
            create myFilters.py

                from  django import template
                register = template.Library()
                def cutlast(value, elements):
                    return value[:len(value) - elements] + "Nazmul Hossain"
                register.filter("myCut", cutlast)
                # myCut is my customtag which will be used in template


        -->5: templates

            {% load myFilters %} 
            <h1>Hello home</h1>
            {{ data|truncatechars:10|upper }}
            <br>
            {{ data|myCut:t}}

        

```

# Custom simple_tag/ customtag