function handle_season_change() {

    x = document.getElementById("team");

    while (x.options.length) {
        x.remove(0);
    }

    var selector_s = document.getElementById("original_season");
    var selected_season = selector_s.options[selector_s.selectedIndex].text

    $.ajax({
        type: "GET",
        url: "http://localhost:5000/api/" + selected_season + "/teams",
        datatype: "json",
        success: function (data) {
            console.log(data)
            for (var i = 0; i < data.length; i++) {
                var option = document.createElement("option");
                option.text = data[i];
                x.add(option);
            }

        }
    });

}

function generate_result() {
    var selector_original = document.getElementById("original_season");
    var original_se = selector_original.options[selector_original.selectedIndex].text

    var selector_new = document.getElementById("new_season");
    var new_se = selector_new.options[selector_new.selectedIndex].text

    var selector_team = document.getElementById("team");
    var team = selector_team.options[selector_team.selectedIndex].text

    $('#result').empty()

    $.ajax({
        type: "GET",
        url: "http://localhost:5000/api/equivalent/" + original_se + "/" + team + "/" + new_se,
        datatype: "json",
        success: function (data) {
            console.log(data.new)
            new_ = Object.values(data.new)
            original_ = Object.values(data.original)

            var rows = "<tr><th>Original</th><th>New</th></tr>"

            for (var i = 0; i < new_.length; i++) {
                rows += '<tr><td>' + original_[i] + '</td><td>' + new_[i] + '</td></tr>';
            }

            $('#result').html(rows);
        }
    });

}