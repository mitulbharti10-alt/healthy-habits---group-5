@anvil.server.callable
def add_task(text):
  app_tables.tasks.add_row(title=text, done=False)

@anvil.server.callable
def get_tasks():
  # Use client_writable() if you want to allow users to check/uncheck boxes directly
  return app_tables.tasks.client_writable().search()
