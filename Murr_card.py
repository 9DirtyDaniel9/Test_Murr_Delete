    def delete(self, request):
        """Можно попробовать так, но я  не уверен, что это будет получать объект."""
        #murr = MurrCard.id
        murr = MurrCard.objects.get(id=request.data['murr_id'])
        print(murr)
        author = request.data['owner_id']
        print(author)
        login_user = request.user.id
        print(login_user)
        """Конвертация в инт, так как при получении из пост запроса прилетает объект типа str."""
        """Respons будут заменены"""
        if int(author) == login_user:
            murr.delete()
            return Response('Successful')
        else:
            return Response('Is it not')
