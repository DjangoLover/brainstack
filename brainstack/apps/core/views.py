from django.core.urlresolvers import reverse
from django.contrib.auth import login, authenticate
from django.views.generic import FormView, TemplateView
from django.shortcuts import redirect

from core.choices import ROLE
from core.models import Project, Participation
from core.forms import ProjectUsernameForm, UsernameForm


class HomeView(FormView):
    form_class = ProjectUsernameForm
    template_name = 'index.html'

    def form_valid(self, form):
        project, user = form.save()
        user = authenticate(username=user.username, password=user.temporary_password)
        login(self.request, user)
        self.kwargs['project_id'] = project.id
        return super(HomeView, self).form_valid(form)

    def get_success_url(self):
        return reverse('spa', args=[self.kwargs['project_id']])


class SPAView(TemplateView):
    template_name = 'spa.html'

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated():
            project = Project.objects.get(id=kwargs['project_id'])
            if project.participants.filter(
                user__username=request.user.username).exists():
                return super(SPAView, self).dispatch(request, *args, **kwargs)

        return redirect('home')

    def get_context_data(self, **kwargs):
        context = super(SPAView, self).get_context_data(**kwargs)
        context['project'] = Project.objects.get(id=kwargs['project_id'])
        return context


class SPAJoinView(FormView):
    form_class = UsernameForm
    template_name = 'join_user_form.html'

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated():
            project = Project.objects.get(_hash=kwargs['project_hash'])
            if project.participants.filter(
                user__username=request.user.username).exists():
                self.kwargs['project_id'] = project.id
                return redirect(self.get_success_url())

        return super(SPAJoinView, self).dispatch(request, *args, **kwargs)


    def form_valid(self, form):
        user = form.save()
        project = Project.objects.get(_hash=self.kwargs['project_hash'])
        Participation.objects.create(user=user, project=project, role=ROLE.CONTRIBUTOR)
        user = authenticate(username=user.username, password=user.temporary_password)
        login(self.request, user)
        self.kwargs['project_id'] = project.id
        return super(SPAJoinView, self).form_valid(form)

    def get_success_url(self):
        return reverse('spa', args=[self.kwargs['project_id']])


