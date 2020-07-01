(function( $ ){
  var stock_symbols = "Change_PercentChange, AskRealtime, LastTradePriceOnly, symbol , Name,  Change , PercentChange , Ask";



  $(function() {
    add_accordion('.accordion' , 0);
    sidebar_menu_folding();
    child_pages_folding();
    Change2NewLookup();
    sliderInit();
    carouselInit();
    if ($(".assetsTicker").length)
      get_json_from_yahoo_finance_and_populate('select ' + stock_symbols + ' from yahoo.finance.quotes where symbol in ("GOLD,OIL,INTC,GOOG,TWTR,KO,MCD,IBM,CSCO,SNE,DIS,LNKD,XOM,NKE,MSFT,FB,AAPL.MX,DOW,TTM,SIRI")');


    // Functionality that controls hiding/showing the email signup lightbox
    // Check to see if cookie is set prior to showing email signup after 5 second delay
    // Set cookies if user clicked on the page. Expiration of this cookie till the close tab
    jQuery('#MainContent').click(function() {
      Cookies.set('clicked', 'yes', '');
    });
    jQuery(window).unload(function() {
      Cookies.remove('clicked');
    });

    // Show pop-up
    setTimeout( function(){
      if( Cookies.get('clicked') !== 'yes' && Cookies.get('noti') !== 'closed' ) {
        jQuery('.email-popup-con').fadeIn();
      }
    }  , 40000 );

    // If user closes lightbox set cookie for 30 days to not show again
    jQuery('.nothanks').click(function() {
      Cookies.set('noti', 'closed', { expires: 10 });
      jQuery('.email-popup-con').fadeOut();
    });

    // Find slide with black font
    jQuery('.slide_black').parents('.bannerText').next().find('a').addClass('slide_black');

    // If user closes lightbox set cookie for 30 days to not show again
    jQuery('.nothanks').click(function() {
        Cookies.set('noti', 'closed', { expires: 10 });
        jQuery('.email-popup-con').fadeOut();
    });

  });


  function sliderInit(){
    $('#bxslider').bxSlider({
      controls: true,
      auto: true,
      pause: 5000,
      infiniteLoop: true,
      useCSS: false,
      mode: 'fade',
      nextSelector: '#slider-next',
      prevSelector: '#slider-prev',
      nextText: 'Onward â†’',
      prevText: 'â† Go back'
    });
  }

  function carouselInit(){
    $('#carousel').bxSlider({
      controls: true,
      auto: true,
      pause: 3000,
      slideWidth: 400,
      slideMargin: 0,
      minSlides: 2,
      maxSlides: 3,
      moveSlides: 1,
      onSliderLoad: function () {
        $('#carousel>div:not(.bx-clone)').eq(1).addClass('active-slide');
      },
      onSlideAfter: function ($slideElement, oldIndex, newIndex) {
        $('.slide').removeClass('active-slide');
        $($slideElement).next().addClass('active-slide');
      }
    });
  }

  /* Control of sidebar menu auto-folding */
  function sidebar_menu_folding() {
    $(".sidebar a").each(function(){
      $(this).html($(this).html().replace("&gt; ",""));
    });

    // define if sub-menu item has child
    $('.sub-menu li a').next('ul').parent().addClass('hasChild');
    $('.menu .current-menu-parent').addClass('menu-item-active');


    $(".sidebar .menu").find("li").each(function() {
      var submenu = $(this).find("ul.sub-menu:first");
      if (submenu.length == 1) {
        if (!$(this).hasClass("current-menu-ancestor")) {
          submenu.hide();
        } else {
          $(this).find("a:first").addClass("MenuOpen");
        }

        $(this).find("a:first").click(submenu_toggle); // Attach toggling event to sub-menu link.
      }
    });
  }

  function submenu_toggle() {

    if ($(this).hasClass('MenuOpen')) return false;

    if ($(this).parents('.sub-menu li').length) {
      $('.sub-menu a').removeClass("MenuOpen").next().slideUp(500);
      $('.sub-menu li').removeClass("hasChildOpen");
      $(this).parent().addClass('hasChildOpen');
      $(this).addClass("MenuOpen").next().slideDown(500);
    } else{
      $('.sub-menu li').removeClass("hasChildOpen");
      $('.sub-menu a').removeClass("MenuOpen").next().slideUp(500);
      $('.menu > li > a').removeClass("MenuOpen").next().slideUp(500);

      $(this).addClass("MenuOpen").next().slideDown(500);
      $('.menu > li').removeClass('menu-item-active');
      $(this).parent().addClass("menu-item-active");
    }
    return false;
  }

  /* Control of inner page child topics auto-folding */

  function child_pages_folding() {
    $(".child-content.deep").hide();
    $(".child-title a").click(childpage_toggle); // Attach toggling event to child title link.
    //resize();
  }

  function childpage_toggle() {
    $(this).parent().parent().siblings().find(".child-content.active").hide().removeClass('active');
    $(this).parent().next().toggle().toggleClass('active');

    $(this).parent().parent().siblings().find(".activeper").removeClass('activeper');
    $(this).parent().toggleClass('activeper');
    //resize();
    return false;
  }

  function Change2NewLookup() {
      var en_lang_link = $('#lang_sel_list .icl-en a');
      en_lang_link.attr('href', en_lang_link.attr('href')+'?lang=EN');

    var $fragment = $(".lang_sel_sel");
    $fragment.contents().filter(function(){
      if (this.nodeType != 1  && $.trim(this.nodeValue).length > 0) {
        return $.trim(this.nodeValue);
      }
    }).wrap("<p/>");
    $("#lang_sel_list").prepend("<div class=language_selector_selected>"+  $fragment.html()  + '<span class="arrow">&nbsp;</span>' + "</div>");

    $('.language_selector_selected').bind('click.language_selector_selected_click', language_selector_selected_click);
    function language_selector_selected_click() {
      if($("#lang_sel_list ul").css("display")=="block") $("#lang_sel_list ul").css("display","none");
      else $("#lang_sel_list ul").css("display","block");
    }

    $('body').bind('click.click_on_body', click_on_body);
    function  click_on_body(event) {
      var $event_origin = $(event.target);
      if(!$event_origin.closest('div').is('.language_selector_selected')) {
        $("#lang_sel_list ul").hide();
      }
    }

  }

  function get_json_from_yahoo_finance_and_populate(query){
    var items = [];
    var up_arrow        = '<span class="stock_img imgup"></span>',
        down_arrow      = '<span class="stock_img imgdown"></span>',
        stockup_class   = '<span class="stockup">',
        stockdown_class = '<span class="stockdown">',
        time_class      = '<span class="stock_time">';
    var yql = 'https://query.yahooapis.com/v1/public/yql?q=' +
        encodeURIComponent(query)
        + '&format=json&callback=?&env=store%3A%2F%2Fdatatables.org%2Falltableswithkeys';

    $.getJSON(yql, json_callback)
        .success    (_json_success)
        .error      (_json_error)
        .complete   (_json_complete);

    function _json_success()    { }
    function _json_error()      { }
    function _json_complete()   { $("ul#stocks").webTicker({travelocity: 0.08});  }


    function json_callback(data) {
      $.each(data.query.results.quote, _loop_results);
      $('#stocks-container').append('<ul id="stocks">' + items.join('') + '</ul>');
      items = [];
    }

    function _json_OBJ_to_sting(value) {
      if (typeof value === 'object') return JSON.stringify(value);
      else if (typeof value === 'string') return value;
      else return value.type;
    }

    function _loop_results(key, val) {
      var direction, ask_type, ask_val, change_type, full_date;
      if(val.symbol.match(/\^/))  ask_val =  _json_OBJ_to_sting(val.LastTradePriceOnly);
      else ask_val =  _json_OBJ_to_sting(val.AskRealtime);

      if(val.Change_PercentChange.match(/\+/)) {
        direction   = up_arrow;
        ask_type    = stockup_class + ask_val +  '</span>';
        change_type = stockup_class + val.Change_PercentChange + '</span>';
      } else {
        direction   = down_arrow;
        ask_type    = stockdown_class + ask_val +  '</span>';
        change_type = stockdown_class + val.Change_PercentChange + '</span>';
      }

      var date = (val.LastTradeDate != null) ? val.LastTradeDate.replace(/\/[\d]{4}/, "").replace(/\//g, ".") : null;
      var time = (val.LastTradeTime != null) ? val.LastTradeTime.replace(/[(am|pm)]+/, "") : null;
      full_date = time_class + "(" + time + " " + date + ")" + '</span>';

      items.push(
          '<li id="' + key + '">' + direction +
          '<strong class="stock_value">' + val.symbol + '</strong>' +
          //ask_type +
          change_type +
          //full_date +
          '</li>');
    }
  }

  function add_accordion(accordion , default_panel){
    $(accordion).attr('id', 'accordion_ui'); //Hook the css

    var allPanels = $(accordion + ' > div').hide();
    var allHeaders = $(accordion + ' > p');
    var defaultPanel =  $(accordion + '> p:eq('+default_panel+')');

    allHeaders.append("<i></i>");//add icon
    defaultPanel.next().slideDown(); // Open default panel
    defaultPanel.addClass("active"); // Add Active class to the default panel

    allHeaders.click(function() {
      if  (!$(this).hasClass( "active" ))
      {
        allPanels.slideUp();
        allHeaders.removeClass('active');
        $(this).next().slideDown();
        $(this).addClass("active");
      }
      else
      {
        $(this).removeClass('active');
        $(this).next().slideUp();
      }
    });
  }




})( jQuery );