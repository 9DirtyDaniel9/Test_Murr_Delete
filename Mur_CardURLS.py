urlpatterns = [
    path('', csrf_exempt(MurrCardView.as_view()), name='MurrCardView'),
    path('save_editor_image/', csrf_exempt(EditorImageForMurrCardView.as_view()), name='save_editor_image'),
    path('all/', csrf_exempt(AllMurr.as_view()), name='all_murrr'),
    #path(r'^murr_card/(?P<pk>\d+)/$', MurrCardView.as_view(), name='delete_murr'),
