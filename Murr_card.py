    def delete(self, request):
        #post = MurrCard.objects.get(id=request.GET.get(murr_id))
        """Получает конкретный пост"""
        murr = MurrCard.objects.get(id=request.query_params['murr_id'])
        """"Получает автора поста"""
        author = murr.owner_id
        """Проверка на соответствие"""
        login_user = request.user.id
        #print(login_user)
        #print(author)
        if author == login_user:
            murr.delete()
            return Response('Hi')
        else:
            return Response('Ni Hao')
