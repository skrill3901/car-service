import { FC, useCallback, useEffect, useMemo, useRef } from 'react';
import { observer } from 'mobx-react-lite';

import { Select } from 'antd';

import { registrationForRepairsState } from '../../model';
import { FieldProps } from './types';

export const MaintenancesField: FC<FieldProps> = observer(({ value, onChange }) => {
  const { maintenances, currentCarId } = registrationForRepairsState;

  const initialRender = useRef(true);

  useEffect(() => {
    if (currentCarId && initialRender.current) {
      registrationForRepairsState.getMaintenances(currentCarId);
      initialRender.current = false;
    }
  }, [currentCarId]);

  const handleChange = useCallback(
    (newValue: number) => {
      const currentMaintenance = maintenances.find((item) => item.id === newValue) || null;

      registrationForRepairsState.setCurrentMaintenance(currentMaintenance);
      onChange?.(newValue);
    },
    [maintenances, onChange]
  );

  const maintenancesToSelect = useMemo(() => {
    return maintenances.map((item) => ({
      value: item.id,
      label: item.operation,
    }));
  }, [maintenances]);

  return <Select value={value} options={maintenancesToSelect} onChange={handleChange} />;
});
