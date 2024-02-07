1. Создание Workspace
   Права доступа: авторизован \
   Cоздать Workspace, к нему создать WorkspaceRole, \
   где User, отправивший запрос будет OWNER
2. Добавление ADMIN
   Права доступа: OWNER
   Update Workspace вида
    ```json
    {
        "id":2,
        "title": "Проект",
        "description": "Описание",
        "admins": [2,4],
        "members": [1,3]
   }
   ```
   Согласно значению admins и members, мы создаем или удаляем \
   записи WorkspaceRole


3. Добавление MEMBER
   Права доступа: OWNER
   Update Workspace вида
    ```json
    {
        "id":2,
        "members": [1,3]
   }
   ```
   Согласно значению members, мы создаем или удаляем \
   записи WorkspaceRole
