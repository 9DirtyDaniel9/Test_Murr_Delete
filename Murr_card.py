    def delete(self, request, *args, **kwargs):
        author_murr = request.data['username']
        """Это не работает, возвращает всегда False"""
        #user = request.data.get("owner")
        login_user = self.request.user.username
        self.object = self.get_object(author_murr)

        if login_user == self.object:
            murr = MurrCard.objects.filter(id=request.query_params['murr_id'])
        #murr = MurrCard.object.get.all()
            murr.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        return Response(status=status.HTTP_400_BAD_REQUEST)
