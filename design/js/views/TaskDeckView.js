var app = app || {};

app.TaskDeckView = Backbone.View.extend({
    el: '#task-deck',
    initialize: function( initialTasks ) {
        this.collection = new app.TaskDeck();
        this.collection.fetch({reset: true});
        this.render();

        this.listenTo(this.collection, 'add', this.renderTask)
        this.listenTo(this.collection, 'reset', this.render)
    },
    render: function() {
        this.collection.each(function( item ) {
            this.renderTask( item );
        }, this );
    },
    renderTask: function( item ) {
        var taskView = new app.TaskView({
            model: item
        });
        console.log(this.$el);
        this.$el.child('$task-list').append(taskView.render().el);
    },
    events: {
        'click #js-open-popup-add': 'showPopupTask',
        'click #js-task-add': 'submitForm',
        'submit #js-form': 'createTask'
    },
    showPopupTask: function(e) {
        var $popup = $('.js-popup-task-add');
        e.preventDefault();
        
        //FIMXE: there should be ability to hide this window
        $popup.toggle();
        //$popup.hide();       
        //    //$popup.fadeIn('slow');
        //$popup.animate({ height: "show"}, 500, function() {});
    },
    submitForm: function(e) {
        var $form = $(e.target).closest('form');
        $form.submit();
    },
    createTask: function(e) {
        e.preventDefault();
    }
});
