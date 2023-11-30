from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required

from item.models import Item
from .models import Conversation
from .forms import ConversationMessageForm

@login_required
def new_conversation(request, item_pk):
    item = get_object_or_404(Item, pk=item_pk)

    if item.created_by == request.user:
        return redirect('dashboard:index')
    
    conversation = Conversation.objects.filter(
        item=item).filter(members__in=[request.user.id]).first()

    if conversation:
        return redirect('conversation:detail', 
            conversation_pk=conversation.id)

    if request.method == 'POST':
        form = ConversationMessageForm(request.POST)

        if form.is_valid():
            conversation = Conversation.objects.create(item=item)
            conversation.members.add(request.user)
            conversation.members.add(item.created_by)
            conversation.save()

            conversation_message = form.save(commit=False)
            conversation_message.conversation = conversation
            conversation_message.created_by = request.user
            conversation_message.save()

            return redirect('item:detail', pk=item_pk)
    
    #else

    form = ConversationMessageForm()

    return render(request, 'conversation/new.html', {

        'form': form,
    })

@login_required
def inbox(request):
    conversations = Conversation.objects.filter(
        members__in=[request.user.id])
    
    #TODO: Show only the N most recent conversations
    #TODO: check if there is a way of doing the code below in a single query, maybe equivalent to join

    conversations_data = [{'conversation': conversation, 
        'last_message': conversation.messages.order_by('-created_at').first()
        } for conversation in conversations]
    
    return render(request, 'conversation/inbox.html', {
        'conversations_data': conversations_data,
    })

@login_required
def detail(request, conversation_pk):
    conversation = Conversation.objects.get(pk=conversation_pk)

    if request.method == 'POST':
        form = ConversationMessageForm(request.POST)

        if form.is_valid():
            conversation_message = form.save(commit=False)
            conversation_message.conversation = conversation
            conversation_message.created_by = request.user
            conversation_message.save()

            # update modified datetime of the conversation
            conversation.save()

            return redirect('conversation:detail', conversation_pk=conversation_pk)
        
    #else

    form = ConversationMessageForm()

    return render(request, 'conversation/detail.html', {
        'conversation': conversation,
        'form': form,
    })