

         fetch('https://api.tibiadata.com/v2/characters/astram%20tempest.json')
        .then(response=> response.json() )
        .then(data =>
          {
            var C1_name =(data.characters.data.name);
            var C1_lvl ="Nivel: " +(data.characters.data.level);
            var C1_voc =(data.characters.data.vocation);
            var C1_prelog =(data.characters.data.last_login[0].date);
            var C1_log ="Last login: "+ C1_prelog.slice(0,-7) + " CEST"
            $("#C1charname").append(C1_name);
            $("#C1charlvl").append(C1_lvl);
            $("#C1charvoc").append(C1_voc);
            $("#C1charlog").append(C1_log);
            }); //end THEN response


         fetch('https://api.tibiadata.com/v2/characters/digibyte%20script.json')
        .then(response=> response.json() )
        .then(data =>
          {
            var C2_name =(data.characters.data.name);
            var C2_lvl ="Nivel: " +(data.characters.data.level);
            var C2_voc =(data.characters.data.vocation);
            var C2_prelog =(data.characters.data.last_login[0].date);
            var C2_log = "Last login: "+C2_prelog.slice(0,-7) + " CEST"
            $("#C2charname").append(C2_name);
            $("#C2charlvl").append(C2_lvl);
            $("#C2charvoc").append(C2_voc);
            $("#C2charlog").append(C2_log);

            }); //end THEN response

         fetch('https://api.tibiadata.com/v2/characters/hemwig.json')
        .then(response=> response.json() )
        .then(data =>
          {
            var C3_name =(data.characters.data.name);
            var C3_lvl ="Nivel: " +(data.characters.data.level);
            var C3_voc =(data.characters.data.vocation);
            var C3_prelog =(data.characters.data.last_login[0].date);
            var C3_log = "Last login: "+C3_prelog.slice(0,-7) + " CEST"
            $("#C3charname").append(C3_name);
            $("#C3charlvl").append(C3_lvl);
            $("#C3charvoc").append(C3_voc);
            $("#C3charlog").append(C3_log);
            }); //end THEN response
