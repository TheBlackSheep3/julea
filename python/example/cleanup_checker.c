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

	kv = j_kv_new("python", "value");
	j_kv_get(kv, &value, &length, batch);
	if (j_batch_execute(batch))
	{
		printf("value written by Python was not removed correctly");
		j_kv_delete(kv, batch);
		j_batch_execute(batch);
	}

	kv = j_kv_new("c", "value");
	j_kv_get(kv, &value, &length, batch);
	if (j_batch_execute(batch))
	{
		printf("value written by C was not removed correctly");
		j_kv_delete(kv, batch);
		j_batch_execute(batch);
	}

	return 0;
}
