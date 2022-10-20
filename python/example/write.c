#include <julea.h>
#include <julea-kv.h>

#include <locale.h>
#include <stdio.h>

int
main()
{
	g_autoptr(JBatch) batch = NULL;
	g_autoptr(JKV) kv = NULL;

	setlocale(LC_ALL, "C.UTF-8");

	batch = j_batch_new_for_template(J_SEMANTICS_TEMPLATE_DEFAULT);

	g_autofree gpointer value = NULL;
	guint32 length = 0;

	kv = j_kv_new("c", "value");
	gchar const* value = "Hello from C :)";
	j_kv_put(kv, g_strdup(value), strlen(value) + 1, g_free, batch);
	if (j_batch_execute(batch))
	{
		return 0;
	}

	return 1;
}
