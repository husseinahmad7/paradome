from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.http.response import Http404
from django.urls import reverse
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin
from .models import ChatChannel, ChatMessage
from .forms import ChatMessageCreation,ChatChannelCreation
from Domes.models import Category

class ChatMessageList(LoginRequiredMixin, generic.ListView,generic.edit.FormMixin):
    template_name = 'chat/chat_messages.html'
    model = ChatMessage
    context_object_name = 'messages'
    paginate = 10
    form_class = ChatMessageCreation
    
    def get_channel_obj(self, pk):
        try:
            return ChatChannel.objects.get(pk=pk)
        except ChatChannel.DoesNotExist:
            raise Http404
    def get_context_data(self, **kwargs):
        context = super(ChatMessageList,self).get_context_data(**kwargs)
        channel = self.get_channel_obj(self.kwargs.get('pk'))
        messages = ChatMessage.objects.filter(channel=channel).order_by('-date')
        # form = self.get_form()
        channel_id = channel.id
        context['channel_id'] = channel_id
        context['messages'] = messages
        # context['form']= form
        return context
    
    def post(self, request, *args, **kwargs):
        form = ChatMessageCreation(self.request.POST, self.request.FILES)
        if form.is_valid():
            body = form.cleaned_data.get('body')
            file = form.cleaned_data.get('file')
            sender = self.request.user
            channel= self.get_channel_obj(self.kwargs.get('pk'))
            
            m, created = ChatMessage.objects.get_or_create(user=sender, body=body, file=file, channel=channel)
            m.save()
            return HttpResponseRedirect(reverse('chat:chat-channel',args=[channel.id]))
        
class ChatChannelCreateView(LoginRequiredMixin, generic.DetailView, generic.edit.FormMixin):
    model = Category
    form_class = ChatChannelCreation
    def post(self, *args, **kwargs):
         form = ChatChannelCreation(self.request.POST)
         if form.is_valid():
             chtchnl_category = self.get_object()
             title = form.cleaned_data['title']
             topic = form.cleaned_data['topic']
             chatchannel = ChatChannel(title=title,topic=topic,category= chtchnl_category)
             chatchannel.save()
             return HttpResponseRedirect(reverse('domes:dome-detail', args=[chtchnl_category.Dome.id]))