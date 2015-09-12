/**
 * Created by wt on 2015/8/30.
 */

    $(function() {
        var graphwidth = $('.widget_graph .inner').width();
        $('.widget_graph .graph').css('height', parseInt(graphwidth/1.7));
        $(window).resize(function() {
            graphwidth = $('.widget_graph .inner').width();
            $('.widget_graph .graph').css('height', parseInt(graphwidth/1.7));
        });

        var d1 = [[0, 9], [1, 23], [1.8, 7], [2.2, 24], [2.8, 18], [4, 36]];
        var graphholder = $("#graph");
        var plot = $.plot(graphholder, [d1], {
            colors: ["#c06030", "#afd8f8", "#cb4b4b", "#4da74d", "#9440ed"],
            xaxis: {
                min: null,
                max: null
            },
            yaxis: {
                autoscaleMargin: 0.02
            },
            series: {
                lines: {
                    show: true,
                    lineWidth: 5,
                    fill: true,
                    fillColor: "rgba(69,144,161,0.1)"
                },
                points: {
                    show: true,
                    radius: 5,
                    lineWidth: 3,
                    fillColor: "#f3d4a4"
                }
            },
            grid: {
                hoverable: true,
                clickable: true,
                margin: 12,
                color: "#79889a",
                borderColor: "#79889a"
            }
        });

        function showTooltip(x, y, contents) {
            $("<div id='graph-tooltip'>" + contents + "</div>").css({top: y - 40, left: x - 22}).appendTo("body").fadeIn(200);
        };

        var previousPoint = null;
        $("#graph").bind("plothover", function (event, pos, item) {

            if (item) {
                if (previousPoint != item.dataIndex) {

                    previousPoint = item.dataIndex;

                    $("#graph-tooltip").remove();
                    var x = item.datapoint[0].toFixed(2),
                            y = item.datapoint[1].toFixed(2);

                    showTooltip(item.pageX, item.pageY, '$' + y*100);
                }
            } else {
                $("#graph-tooltip").remove();
                previousPoint = null;
            }
        });
    });
