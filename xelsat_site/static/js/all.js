	$(document).ready(function(){
  $("#owl").owlCarousel({
      autoplay:true,
      autoplayTimeout:4000,
      autoplayHoverPause:true,
      loop:true,
      items:1 ,
      pagination: true,
      nav: false
  });
   $(".block-wrapper .partner-info").responsiveEqualHeightGrid();
   $(".footer-box").responsiveEqualHeightGrid();
   $("#scroll1").niceScroll();
   $(".for-dropdown, .dropdown").hover(
          function(){
          $(".dropdown").addClass("block"),
          $(".for-dropdown").addClass("active");
    });
   $(".dropdown").mouseleave(function(){
          $(".dropdown").removeClass("block");
          $(".for-dropdown").removeClass("active");

   });
   $(".first-link, .third-link, .header-bottom").hover(
          function(){
          $(".dropdown").removeClass("block");
          $(".for-dropdown").removeClass("active");
  })


   $('.for-satellite-drop, .for-satellite-drop:before, .bucs-drop, .converters-drop').hover(
    function(){
        $('.satellite-drop').addClass("block");
    },
    function(){
        $('.satellite-drop').removeClass("block");
    });


    $('.for-networks-drop, .for-networks-drop:before').hover(
    function(){
        $('.networks-drop').addClass("block");
    },
    function(){
        $('.networks-drop').removeClass("block");
    });



    $('.for-bucs-drop, .for-bucs-drop:before, .converters-drop').hover(
    function(){
        $('.bucs-drop').addClass("block");
    },
    function(){
        $('.bucs-drop').removeClass("block");
    });

    $('.for-converters-drop, .for-converters-drop:before').hover(
    function(){
        $('.converters-drop').addClass("block");
    },
    function(){
        $('.converters-drop').removeClass("block");
    });
   $("#owl-second").owlCarousel({
      items : 4, 
      loop:true,
      pagination: false,
      nav: true,
      responsive:{
        0:{
            items:1
        },
        600:{
            items:2
        },
        1000:{
            items:3
        },
        1200:{
            items:4
        }
       }
  });
   $("#owl-third").owlCarousel({
      autoplay:true,
      autoplayTimeout:4000,
      items:3,
      pagination: false,
      navigation: false,
      responsive:{
        0:{
            items:1
        },
        600:{
            items:2
        },
        1000:{
            items:3
        }
       }
  });

  var sync1 = $('#sync1'),
    sync2 = $('#sync2'),
    duration = 0.001,
    thumbs = 4;

// Sync nav
sync1.on('click', '.owl-next', function () {
    sync2.trigger('next.owl.carousel')
});
sync1.on('click', '.owl-prev', function () {
    sync2.trigger('prev.owl.carousel')
});

// Start Carousel
sync1.owlCarousel({
    rtl: true,
    center : true,
    loop: true,
    items : 1,
    margin:0,
    nav : false
})
.on('dragged.owl.carousel', function (e) {
        if (e.relatedTarget.state.direction == 'left') {
            sync2.trigger('next.owl.carousel')
        } else {
            sync2.trigger('prev.owl.carousel')
        }
});


sync2.owlCarousel({
    rtl: true,
    loop: true,
    items: 4,
    items : thumbs,
    nav : false
})
.on('click', '.owl-item', function() {
    var i = $(this).index()-(thumbs+1);
    sync2.trigger('to.owl.carousel', [i, duration, true]);
    sync1.trigger('to.owl.carousel', [i, duration, true]);
});
 
  $('select').selectpicker();
    var offset = $('#sticky-header').offset();
  $(window).scroll(function(){
    $('#sticky-header').addClass('fixed-header');
    $('#dropdown').addClass('fixed-dropdown');
    $('#collapseSearch').addClass('fixed-search');
    if($(document).scrollTop() < 20){
    $('#sticky-header').removeClass('fixed-header');
    $('#dropdown').removeClass('fixed-dropdown');
    $('#collapseSearch').removeClass('fixed-search');
    }
     });
    $('#myTab a').click(function (e) {
      e.preventDefault()
      $(this).tab('show')
    })
});

/*button to-top*/
$(function() {
  $(window).scroll(function() {
  if($(this).scrollTop() != 0) {
  $('#toTop').fadeIn();
  } else {
  $('#toTop').fadeOut();
  }
  });
  $('#toTop').click(function() {
  $('body,html').animate({scrollTop:0},800);
  });
});
 $(document).click( function(event){
      if( $(event.target).closest("#collapseSearch").length ) 
        return;
      $("#collapseSearch").removeClass("in");
      event.stopPropagation();
    });