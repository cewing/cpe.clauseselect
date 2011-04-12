function toTitleCase(str) {
    return str.replace(/\w\S*/g, function (txt) {return txt.charAt(0).toUpperCase() + txt.substr(1).toLowerCase(); });
}


function handleSelectableClick(clicked, container) {
    var trg, sel, pop, txt, opt;
    trg = container.find('a.clause_trigger');
    sel = container.find('select');
    pop = container.find('ul.clause_popup');
    txt = clicked.text();
    // set trigger text to selected element text:
    trg.text(txt);
    // set value of the select (and unset previously selected):
    sel.find("option:selected").removeAttr("selected");
    // we have to set our selected option by text because text and value
    // _do_not_ always match
    opt = sel.find("option:contains('" + txt + "')");
    opt.attr("selected", "selected");
    // unselect any selected elements in the popup:
    pop.find('a.clause_selectable').removeClass('selected');
    clicked.addClass('selected');
    if (trg.data('tooltip')) {
        trg.data('tooltip').hide();
    }
}

// set a click handler as high up the DOM tree as feasible
function clauseSelectClickHandler(e) {
    var target, container, form;
    target = $(e.target);
    if (target.is('a.clause_selectable')) {
        e.preventDefault();
        container = target.parents('li.clause:first');
        handleSelectableClick(target, container);
        form = target.parents('form:first');
        form.submit();
    } else if (target.is('a.clause_trigger')) {
        e.preventDefault();
    } else if (target.is('a.clause_refinements_link')) {
        e.preventDefault();
    } else if (target.is('a.dual_map_toggle')) {
        e.preventDefault();
    }
}

// given a jQuery object containing a clause select element, return a jquery 
// object containing a trigger for it.
function createClauseTrigger(select) {
    var id, val, trig, txt;
    id = select.attr('id');
    val = select.val();
    trig = $('<a id="' + id + '-trigger" class="clause_trigger" href="#" />');
    txt = select.find('option:selected').text();
    trig.text(txt);
    return trig;
}

// given a jquery object containing a clause select, return a jquery object
// containing the popup selectable mated to that select
function createClausePopup(select) {
    var id, popup;
    id = select.attr('id');
    popup = $('<ul id="' + id + '-popup" class="clause_popup" />');
    select.find('option').each(function () {
        var opt, item, link;
        opt = $(this);
        item = $('<li><a href="#" class="clause_selectable" /></li>');
        link = item.find('a');
        link.text(opt.text());
        if (opt.attr('selected')) {
            link.addClass('selected');
        }
        popup.append(item);
    });
    return popup;
}

function commonClauseSetup(select) {
    var id, wrapper_id;
    id = select.attr('id');
    wrapper_id = id + '-container';
    select.parent().addClass("clause").attr('id', wrapper_id);
    select.before(createClauseTrigger(select))
        .before(createClausePopup(select));
    select.css('display', 'none');
}

function refinementClauseSetup(select) {
    var parent, trig, trig_txt, label;
    select.removeClass('refinement');
    parent = select.parent();
    parent.addClass('refinement');
    trig = parent.find('a.clause_trigger');
    trig_txt = trig.text().replace('all ', '');
    trig.text(toTitleCase(trig_txt));
    label = parent.find('label');
    label.css('display', 'none');
}

// given a clause select element, wrap it in the appropriate structure
function buildClauseSelect(idx, elem) {
    var select;
    select = $(elem);
    commonClauseSetup(select);
    if (select.hasClass('refinement')) {
        refinementClauseSetup(select);
    }
}

function buildRefinementPopup(idx, ul) {
    var cls, popup, poptrig, poplink, poplist;
    cls = 'clause_refinements';
    popup = $('<li />').addClass(cls);
    poptrig = $('<p />').addClass(cls + '_header');
    poplink = $('<a />').attr('href', '#')
        .addClass(cls + '_link')
        .text('Refine Further');
    poplist = $('<ul />').addClass(cls + '_fields');
    $(ul).find('li.clause.refinement').appendTo(poplist);
    poptrig.append(poplink);
    popup.append(poptrig).append(poplist);
    popup.appendTo($(ul));
}

function formatClauseSelects(form) {
    $(form).find('select.clause_select').each(buildClauseSelect);
    $(form).find('ul.clause_sentence').each(buildRefinementPopup);
}

function activateClauses(form) {
    $(form).find('a.clause_trigger').tooltip({
        position: 'bottom right',
        events: {
            def: "click, mouseout",
            tooltip: "mouseover, mouseout",
            a: 'click, click'
        },
        delay: 500,
        relative: true,
        onBeforeShow: function (e, pos) {
            var trig, twidth, conf;
            trig = this.getTrigger();
            twidth = trig.innerWidth();
            conf = this.getConf();
            conf.offset[1] = -twidth;
        }
    });
    $(form).find('p.clause_refinements_header a').tooltip({
        position: 'bottom right',
        events: {
            def: "click, mouseout",
            tooltip: "mouseover, mouseleave"
        },
        delay: 500,
        relative: true,
        onBeforeShow: function (e, pos) {
            var trig, twidth, conf;
            trig = this.getTrigger();
            twidth = trig.innerWidth();
            conf = this.getConf();
            conf.offset[0] = -1;
            conf.offset[1] = -2 - twidth;
        }
    });
    $(form).unbind('click');
    $(form).click(clauseSelectClickHandler);
}
