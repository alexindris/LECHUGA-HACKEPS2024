import 'package:flutter/material.dart';

class SampleItemDetailsView extends StatelessWidget {
  static const routeName = '/item-details';

  const SampleItemDetailsView({super.key});

  @override
  Widget build(BuildContext context) {
    final parking =
        ModalRoute.of(context)?.settings.arguments as Map<String, dynamic>;

    return Scaffold(
      appBar: AppBar(
        title: Text(parking['name']),
      ),
      body: Padding(
        padding: const EdgeInsets.all(16.0),
        child: Column(
          crossAxisAlignment: CrossAxisAlignment.start,
          children: [
            Text('Identifier: ${parking['identifier']}',
                style: Theme.of(context).textTheme.titleLarge),
            const SizedBox(height: 8),
            Text('Address: ${parking['address']}'),
            const SizedBox(height: 8),
            Text('Total Lots: ${parking['totalLots']}'),
            Text('Occupied Lots: ${parking['occupiedLots']}'),
          ],
        ),
      ),
    );
  }
}
